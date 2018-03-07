"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["a b c", 3],
            "answer": "d e f"
        },
        {
            "input": ["a b c", -3],
            "answer": "x y z"
        }
    ],
    "Extra": [
        {
            "input": ["simple text", 16],
            "answer": "iycfbu junj"
        },
        {
            "input": ["important text", 10],
            "answer": "swzybdkxd dohd"
        },
	{
            "input": ["state secret", -13],
            "answer": "fgngr frperg"
        }
    ]
}
