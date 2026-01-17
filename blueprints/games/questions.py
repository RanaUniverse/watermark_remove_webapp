"""
Here i will keep the questions here,
blueprints/games/questions.py
For now i will not do the mcq like things rather i will make one user input
for the answer and check if the answer is correct or not
"""

from typing import TypedDict


class MathQuestion(TypedDict):
    id: int
    question: str
    options: list[str]
    answer: str


math_questions: list[MathQuestion] = [
    {
        "id": 1,
        "question": "2 + 3 + 4 = ?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
    },
    {
        "id": 2,
        "question": "5 * 6 = ?",
        "options": ["11", "30", "56", "60"],
        "answer": "30",
    },
    {
        "id": 3,
        "question": "10 - 4 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "6",
    },
    {
        "id": 4,
        "question": "8 + 7 = ?",
        "options": ["14", "15", "16", "17"],
        "answer": "15",
    },
    {
        "id": 5,
        "question": "9 * 3 = ?",
        "options": ["18", "21", "27", "36"],
        "answer": "27",
    },
    {
        "id": 6,
        "question": "20 / 4 = ?",
        "options": ["4", "5", "6", "8"],
        "answer": "5",
    },
    {
        "id": 7,
        "question": "6 + 6 + 6 = ?",
        "options": ["12", "15", "18", "21"],
        "answer": "18",
    },
    {
        "id": 8,
        "question": "12 + 8 = ?",
        "options": ["18", "19", "20", "21"],
        "answer": "20",
    },
    {
        "id": 9,
        "question": "7 * 4 = ?",
        "options": ["24", "26", "28", "30"],
        "answer": "28",
    },
    {
        "id": 10,
        "question": "15 - 6 = ?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
    },
    {
        "id": 11,
        "question": "9 + 11 = ?",
        "options": ["18", "19", "20", "21"],
        "answer": "20",
    },
    {
        "id": 12,
        "question": "8 * 5 = ?",
        "options": ["35", "40", "45", "50"],
        "answer": "40",
    },
    {
        "id": 13,
        "question": "18 / 3 = ?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
    },
    {
        "id": 14,
        "question": "14 + 5 = ?",
        "options": ["18", "19", "20", "21"],
        "answer": "19",
    },
    {
        "id": 15,
        "question": "7 + 8 + 5 = ?",
        "options": ["18", "19", "20", "21"],
        "answer": "20",
    },
    {
        "id": 16,
        "question": "16 - 9 = ?",
        "options": ["6", "7", "8", "9"],
        "answer": "7",
    },
    {
        "id": 17,
        "question": "6 * 7 = ?",
        "options": ["36", "40", "42", "48"],
        "answer": "42",
    },
    {
        "id": 18,
        "question": "24 / 6 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
    },
    {
        "id": 19,
        "question": "10 + 9 = ?",
        "options": ["18", "19", "20", "21"],
        "answer": "19",
    },
    {
        "id": 20,
        "question": "5 * 5 + 5 = ?",
        "options": ["25", "30", "35", "40"],
        "answer": "30",
    },
    {
        "id": 21,
        "question": "14 * 2 = ?",
        "options": ["26", "28", "30", "32"],
        "answer": "28",
    },
    {
        "id": 22,
        "question": "30 / 5 = ?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
    },
    {
        "id": 23,
        "question": "17 + 6 = ?",
        "options": ["21", "22", "23", "24"],
        "answer": "23",
    },
    {
        "id": 24,
        "question": "20 - 11 = ?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
    },
    {
        "id": 25,
        "question": "4 * 9 = ?",
        "options": ["32", "34", "36", "38"],
        "answer": "36",
    },
    {
        "id": 26,
        "question": "27 / 3 = ?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
    },
    {
        "id": 27,
        "question": "11 + 12 = ?",
        "options": ["21", "22", "23", "24"],
        "answer": "23",
    },
    {
        "id": 28,
        "question": "25 - 7 = ?",
        "options": ["16", "17", "18", "19"],
        "answer": "18",
    },
    {
        "id": 29,
        "question": "6 * 8 = ?",
        "options": ["42", "46", "48", "52"],
        "answer": "48",
    },
    {
        "id": 30,
        "question": "40 / 8 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "5",
    },
    {
        "id": 31,
        "question": "19 + 4 = ?",
        "options": ["21", "22", "23", "24"],
        "answer": "23",
    },
    {
        "id": 32,
        "question": "22 - 9 = ?",
        "options": ["11", "12", "13", "14"],
        "answer": "13",
    },
    {
        "id": 33,
        "question": "7 * 9 = ?",
        "options": ["54", "56", "63", "72"],
        "answer": "63",
    },
    {
        "id": 34,
        "question": "36 / 6 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "6",
    },
    {
        "id": 35,
        "question": "15 + 14 = ?",
        "options": ["27", "28", "29", "30"],
        "answer": "29",
    },
    {
        "id": 36,
        "question": "50 - 18 = ?",
        "options": ["30", "31", "32", "33"],
        "answer": "32",
    },
    {
        "id": 37,
        "question": "8 * 7 = ?",
        "options": ["54", "56", "58", "60"],
        "answer": "56",
    },
    {
        "id": 38,
        "question": "45 / 9 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "5",
    },
    {
        "id": 39,
        "question": "21 + 8 = ?",
        "options": ["27", "28", "29", "30"],
        "answer": "29",
    },
    {
        "id": 40,
        "question": "34 - 16 = ?",
        "options": ["16", "17", "18", "19"],
        "answer": "18",
    },
    {
        "id": 41,
        "question": "9 * 6 = ?",
        "options": ["48", "50", "54", "56"],
        "answer": "54",
    },
    {
        "id": 42,
        "question": "56 / 7 = ?",
        "options": ["6", "7", "8", "9"],
        "answer": "8",
    },
    {
        "id": 43,
        "question": "13 + 17 = ?",
        "options": ["28", "29", "30", "31"],
        "answer": "30",
    },
    {
        "id": 44,
        "question": "60 - 22 = ?",
        "options": ["36", "37", "38", "39"],
        "answer": "38",
    },
    {
        "id": 45,
        "question": "5 * 12 = ?",
        "options": ["50", "55", "60", "65"],
        "answer": "60",
    },
    {
        "id": 46,
        "question": "72 / 8 = ?",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
    },
    {
        "id": 47,
        "question": "26 + 9 = ?",
        "options": ["33", "34", "35", "36"],
        "answer": "35",
    },
    {
        "id": 48,
        "question": "41 - 19 = ?",
        "options": ["20", "21", "22", "23"],
        "answer": "22",
    },
    {
        "id": 49,
        "question": "11 * 4 = ?",
        "options": ["40", "42", "44", "46"],
        "answer": "44",
    },
    {
        "id": 50,
        "question": "100 / 10 = ?",
        "options": ["8", "9", "10", "11"],
        "answer": "10",
    },
]
