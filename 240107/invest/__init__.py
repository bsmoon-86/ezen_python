# 4개의 투자전력 모듈을 로드
from invest.quant import buyandhold as bnh
from invest.quant import bollinger as boll
from invest.quant import momentum as mmt

class Invest:

    # 생성자 함수 
    def __init__(
            self, 
            _data, 
            _col = 'Adj Close', 
            _start = '2010-01-01', 
            _end = '2023-12-31'
        ):
        self.data = _data
        self.col = _col
        self.start = _start
        self.end = _end
    
    # 바이앤홀드 전략 함수를 생성 
    def BuyAndHold(self):
        result, rtn = bnh.buyandhold(
            self.data, 
            self.col, 
            self.start, 
            self.end
        )
        print(f'바이앤홀드 누적 수익율은 {rtn}입니다.')
        return result

    # 볼린져 밴드 함수
    def Bollinger(self, _roll = 20):
        band_df = boll.create_band(
            self.data, 
            self.col, 
            self.start, 
            self.end, 
            _roll
        )
        trade_df = boll.create_trade(
            band_df
        )
        result = boll.create_rtn(
            trade_df
        )
        return result
    
    # 절대 모멘텀 함수 
    def Momentum(self, _momentum = 12, _score=1):
        ym_df = mmt.create_ym(
            self.data, 
            self.col
        )
        month_last_df = mmt.create_month_last(
            ym_df, 
            _momentum, 
            self.start
        )
        trade_df = mmt.create_trade(
            ym_df, 
            month_last_df, 
            _score
        )
        result = mmt.create_rtn(trade_df)
        return result