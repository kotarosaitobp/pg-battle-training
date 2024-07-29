import re

"""
テストケース

4
MFMF

6
MFMFMF

7
MMMFMMM

50
MFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMFMF
"""


def solve(N, S):
    M = S.count("M")
    F = N - M

    if N % 2 == 1:
        return 0

    if M != F:
        return 0

    def find_pair_positions(s):
        pattern = r"(?=(MF|FM))"

        positions = [m.start() for m in re.finditer(pattern, s)]

        return positions

    answer = 1
    while True:
        if S == "":
            break

        positions = find_pair_positions(S)

        answer *= len(positions)

        S = S[: positions[0]] + S[positions[0] + 2 :]  # ここがだいぶ怪しい

    mod = 988244353
    return answer % mod


if __name__ == "__main__":
    # 50が530531691で答えが合わない
    N = int(input())
    S = input()
    result = solve(N, S)
    print(result)
