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
            "input": ["!d! [e] &f*", -3],
            "answer": "a b c"
        },
        {
            "input": ["x^$# y&*( (z):-)", 3],
            "answer": "a b c"
        }
    ],
    "Extra": [
        {
            "input": ["iycfbu!@# junj%&", -16],
            "answer": "simple text"
        },
        {
            "input": ["*$#%swzybdkxd !)(^#%dohd", -10],
            "answer": "important text"
        },
	{
            "input": ["fgngr **&&frperg^__^", 13],
            "answer": "state secret"
        }
    ]
}
