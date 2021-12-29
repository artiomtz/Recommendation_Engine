# Recommendation_Engine
A pair matching system for an optimization course and a component of a design project.


Input JSON structure:
{
  "num_interests": <number of interests>,
  "<user id>": [
    { "<interest id>": <interest rating> },
    { "<interest id>": <interest rating> }
  ],
  "<user id>": [
    { "<interest id>": <interest rating> },
    { "<interest id>": <interest rating> }
  ]
}

Example:
{
  "num_interests": 4,
  "1": [
    { "1": 2 },
    { "2": 4 },
    { "3": 1 },
    { "4": 3 }
  ],
  "2": [
    { "1": 3 },
    { "2": 2 },
    { "3": 5 },
    { "4": 1 }
  ],
  "3": [
    { "1": 1 },
    { "2": 5 },
    { "3": 5 },
    { "4": 2 }
  ]
}


Output structure:
[[<user id>, <user id>], [<user id>, <user id>]]

Example:
[[1, 3], [2, 8], [19, 4]]


The Sample_Data.csv belongs to danielyue (https://github.com/danielyue/cs136roommatch).
