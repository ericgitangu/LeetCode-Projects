class Solution:
    def countTime(self, time: str) -> int:
        hr, mins = time.split(':')
        h_ones, h_tens, m_ones, m_tens = False, False, False, False
        isSix = False
        try:
            if mins.index('?') == 0:
                m_tens = True
            if mins[1:].index('?') == 0:
                m_ones = True
        except:
            pass # ignore mins
        try:
            if hr.index('?') == 0:
                h_tens = True
            if hr[1:].index('?') == 0:
                h_ones = True
            # print(hr, mins, hr.index('?'), mins.index('?'))
        except:
            pass # ignore hrs
        isSixty = m_tens and m_ones    
        isTwentyFour = h_ones and h_tens
        isTwo = h_tens and not h_ones and int('2' + hr[1:]) >= 24
        isThree = h_tens and not h_ones and int('2' + hr[1:]) < 24
        isTenHr = (not h_tens and h_ones) and (hr[0] == '0' or hr[0] == '1')
        isTenMins = (not m_tens and m_ones)
        isSix = (m_tens and not m_ones)
        isFour = (not h_tens and h_ones) and not (hr[0] == '0' or hr[0] == '1')
        isTenHr = (not h_tens and h_ones) and (hr[0] == '0' or hr[0] == '1')
        
        # print(time, isSixty, isTwentyFour, isTwo, isTenHr, isTenMins,isSix, isFour)
        res = 1
        if isSixty:
            res *= 60
        if isTwentyFour:
            res *= 24
        if isTwo:
            res *= 2
        if isThree:
            res *= 3
        if isTenHr:
            res *= 10
        if isTenMins:
            res *= 10
        if isSix:
            res *= 6
        if isFour:
            res *= 4
        return res
        