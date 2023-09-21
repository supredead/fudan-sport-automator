import hashlib
import json
import os
from pathlib import Path

import aiohttp
from geopy.point import Point


def _get_arg_from_env_or_json(arg_name, default=''):
    value = os.getenv(arg_name)
    if value is None or not value.strip():
        # Try loading from settings.json
        try:
            with open(Path(__file__).parent / 'settings.json', 'r', encoding='utf-8') as fp:
                value = json.load(fp)[arg_name]
        except FileNotFoundError:
            print("ERROR: 未导入数据，请检查settings路径")
            exit(1)
    return value


async def get_routes():
    route_url = 'https://sport.fudan.edu.cn/sapi/route/list'
    params = {'userid': _get_arg_from_env_or_json('USER_ID'),
              'token': _get_arg_from_env_or_json('FUDAN_SPORT_TOKEN')}
    params = sign_param(params)
    async with aiohttp.request('GET', route_url, params=params) as response:
        data = await response.json()
    try:
        route_data_list = filter(lambda route: route['points'] is not None and len(route['points']) == 1,
                                 data['data']['list'])
        return [FudanRoute(route_data) for route_data in route_data_list]
    except Exception:
        print(f"ERROR: {data['message']}")
        exit(1)


class FudanAPI:
    def __init__(self, route):
        self.route = route
        self.user_id = _get_arg_from_env_or_json('USER_ID')
        self.token = _get_arg_from_env_or_json('FUDAN_SPORT_TOKEN')
        self.system = _get_arg_from_env_or_json('PLATFORM_OS', 'iOS 2016.3.1')
        self.device = _get_arg_from_env_or_json('PLATFORM_DEVICE', 'iPhone|iPhone 13<iPhone14,5>')
        self.run_id = None

    async def start(self):
        start_url = 'https://sport.fudan.edu.cn/sapi/run/start'
        params = {'userid': self.user_id,
                  'token': self.token,
                  'route_id': self.route.id,
                  'route_type': self.route.type,
                  'system': self.system,
                  'device': self.device,
                  'lng': self.route.start_point.longitude,
                  'lat': self.route.start_point.latitude}
        params = sign_param(params)
        async with aiohttp.request('GET', start_url, params=params) as response:
            data = await response.json()
        try:
            self.run_id = data['data']['run_id']
        except Exception:
            print(f"ERROR: {data['message']}")
            exit(1)

    async def update(self, point):
        update_url = 'https://sport.fudan.edu.cn/sapi/run/point'
        params = {'userid': self.user_id,
                  'token': self.token,
                  'run_id': self.run_id,
                  'lng': point.longitude,
                  'lat': point.latitude}
        params = sign_param(params)
        async with aiohttp.request('GET', update_url, params=params) as response:
            try:
                data = await response.json()
                return data['message']
            except Exception:
                return await response.read()

    async def finish(self, point):
        finish_url = 'https://sport.fudan.edu.cn/sapi/run/finish'
        params = {'userid': self.user_id,
                  'token': self.token,
                  'run_id': self.run_id,
                  'system': self.system,
                  'device': self.device,
                  'lng': point.longitude,
                  'lat': point.latitude}
        params = sign_param(params)
        async with aiohttp.request('GET', finish_url, params=params) as response:
            data = await response.json()
        return data['message']


def sign_param(params):
    keys = sorted(params.keys())
    arr = []
    for k in keys:
        arr.append(str(params[k]))
    vals = ",".join(arr)
    s = "moveclub123123123" + vals
    md5_hash = hashlib.md5()
    md5_hash.update(s.encode('utf-8'))
    params["sign"] = md5_hash.hexdigest()
    return params


class FudanRoute:
    def __init__(self, data):
        self.id = data['route_id']
        self.name = data['name']
        self.type = data['types'][0]
        self.start_point = Point(data['points'][0]['lat'],
                                 data['points'][0]['lng'])

    def pretty_print(self):
        print(f"#{self.id}: {self.name}")
