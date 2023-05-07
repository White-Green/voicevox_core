import numpy as np

# 「こんにちは、音声合成の世界へようこそ」という文章を変換して得た phoneme_vector
example_phoneme_vector = np.array(
    [
        0,
        23,
        30,
        4,
        28,
        21,
        10,
        21,
        42,
        7,
        0,
        30,
        4,
        35,
        14,
        14,
        16,
        30,
        30,
        35,
        14,
        14,
        28,
        30,
        35,
        14,
        23,
        7,
        21,
        14,
        43,
        30,
        30,
        23,
        30,
        35,
        30,
        0,
    ]
)

# 「テスト」という文章に対応する入力
example_vowel_phoneme_vector = np.array([0, 14, 6, 30, 0])
example_consonant_phoneme_vector = np.array([-1, 37, 35, 37, -1])
example_start_accent_vector = np.array([0, 1, 0, 0, 0])
example_end_accent_vector = np.array([0, 1, 0, 0, 0])
example_start_accent_phrase_vector = np.array([0, 1, 0, 0, 0])
example_end_accent_phrase_vector = np.array([0, 0, 0, 1, 0])

TEXT_CONSONANT_VOWEL_DATA1 = [
    ([("コ", "k", "o"), ("レ", "r", "e"), ("ワ", "w", "a")], 3),
    (
        [
            ("テ", "t", "e"),
            ("ス", "s", "U"),
            ("ト", "t", "o"),
            ("デ", "d", "e"),
            ("ス", "s", "U"),
        ],
        1,
    ),
]

TEXT_CONSONANT_VOWEL_DATA2 = [
    ([("コ", "k", "o"), ("レ", "r", "e"), ("ワ", "w", "a")], 1),
    (
        [
            ("テ", "t", "e"),
            ("ス", "s", "U"),
            ("ト", "t", "o"),
            ("デ", "d", "e"),
            ("ス", "s", "U"),
        ],
        3,
    ),
]
