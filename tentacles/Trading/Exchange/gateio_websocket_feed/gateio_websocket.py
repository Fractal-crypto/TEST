#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import octobot_trading.exchanges as exchanges
import cryptofeed.defines as cryptofeed_constants
from octobot_trading.enums import WebsocketFeeds as Feeds


class GateIOCryptofeedWebsocketConnector(exchanges.CryptofeedWebsocketConnector):
    REQUIRED_ACTIVATED_TENTACLES = []
    EXCHANGE_FEEDS = {
        Feeds.TRADES: cryptofeed_constants.TRADES,
        Feeds.KLINE: Feeds.UNSUPPORTED.value,
        Feeds.TICKER: cryptofeed_constants.TICKER,
        Feeds.CANDLE: Feeds.UNSUPPORTED.value,
        Feeds.L2_BOOK: Feeds.UNSUPPORTED.value,
        Feeds.BOOK_DELTA: Feeds.UNSUPPORTED.value,
        Feeds.VOLUME: Feeds.UNSUPPORTED.value,
        Feeds.OPEN_INTEREST: Feeds.UNSUPPORTED.value,
    }

    @classmethod
    def get_name(cls):
        return 'gateio'

    @classmethod
    def get_feed_name(cls):
        return cryptofeed_constants.GATEIO

    @classmethod
    def is_handling_spot(cls) -> bool:
        return True
