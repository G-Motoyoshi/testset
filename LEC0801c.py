# ライブラリのインポート
import random
import time

# 問1. 1 ～ 10 までの乱数を一度に３つ発生させて、最も小さな値の秒数処理を止める関数を作成せよ。
def stoptime():
    """ここにこの関数の注釈を書く"""
    # ここに作成せよ
    rlist = [random.randint(1, 10) for i in range(3)]
    return time.sleep(min(rlist))

# 問2. 1 ～ 10 までの乱数を発生させ、その合計が 100 を超えるまでループするアルゴリズムを作成せよ。
# 毎回合計値を出力し、100 を超えた場合「終了」と知らせよ。
# ここに作成せよ
if __name__ == '__main__':
    summu = 0
    while summu < 100:
        summu += random.randint(1, 10)
        print(summu)
    print('終了')

# 問3. 現在時刻を表示させよ。
if __name__ == "__main__":
    # ここに作成せよ
    print(time.time())