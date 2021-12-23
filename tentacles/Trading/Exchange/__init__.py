from octobot_tentacles_manager.api.inspector import check_tentacle_version
from octobot_commons.logging.logging_util import get_logger

if check_tentacle_version('1.2.0', 'ascendex', 'OctoBot-Default-Tentacles'):
    try:
        from .ascendex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading ascendex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'hitbtc', 'OctoBot-Default-Tentacles'):
    try:
        from .hitbtc import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading hitbtc: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'default_spot_ccxt', 'OctoBot-Default-Tentacles'):
    try:
        from .default_spot_ccxt import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading default_spot_ccxt: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'kucoin', 'OctoBot-Default-Tentacles'):
    try:
        from .kucoin import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading kucoin: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'ftx_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .ftx_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading ftx_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'kucoin_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .kucoin_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading kucoin_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'okex', 'OctoBot-Default-Tentacles'):
    try:
        from .okex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading okex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bitmex', 'OctoBot-Default-Tentacles'):
    try:
        from .bitmex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bitmex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'binanceus_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .binanceus_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binanceus_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bitstamp', 'OctoBot-Default-Tentacles'):
    try:
        from .bitstamp import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bitstamp: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bittrex', 'OctoBot-Default-Tentacles'):
    try:
        from .bittrex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bittrex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'ftx', 'OctoBot-Default-Tentacles'):
    try:
        from .ftx import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading ftx: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bithumb', 'OctoBot-Default-Tentacles'):
    try:
        from .bithumb import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bithumb: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'coinbase_pro_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .coinbase_pro_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading coinbase_pro_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'gateio_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .gateio_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading gateio_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'gateio', 'OctoBot-Default-Tentacles'):
    try:
        from .gateio import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading gateio: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'kraken', 'OctoBot-Default-Tentacles'):
    try:
        from .kraken import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading kraken: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'wavesexchange', 'OctoBot-Default-Tentacles'):
    try:
        from .wavesexchange import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading wavesexchange: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'okex_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .okex_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading okex_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'coinbase_pro', 'OctoBot-Default-Tentacles'):
    try:
        from .coinbase_pro import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading coinbase_pro: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'binanceus', 'OctoBot-Default-Tentacles'):
    try:
        from .binanceus import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binanceus: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'binance', 'OctoBot-Default-Tentacles'):
    try:
        from .binance import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binance: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bybit', 'OctoBot-Default-Tentacles'):
    try:
        from .bybit import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bybit: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'ascendex_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .ascendex_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading ascendex_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bitfinex', 'OctoBot-Default-Tentacles'):
    try:
        from .bitfinex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bitfinex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'binance_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .binance_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binance_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'huobi_websocket_feed', 'OctoBot-Default-Tentacles'):
    try:
        from .huobi_websocket_feed import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading huobi_websocket_feed: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'crex24', 'OctoBot-Default-Tentacles'):
    try:
        from .crex24 import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading crex24: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'okcoin', 'OctoBot-Default-Tentacles'):
    try:
        from .okcoin import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading okcoin: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')
