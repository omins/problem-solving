answers = [1, 2, 3, 4, 5];
expectedAnswer = [1];

function solution(answers) {
  let answer = [];

  const pattern = {
    1: [1, 2, 3, 4, 5],
    2: [2, 1, 2, 3, 2, 4, 2, 5],
    3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  };

  const stud = {
    1: [],
    2: [],
    3: [],
  };

  let curMax = 0;

  for (let i = 1; i <= 3; i++) {
    let cnt = 0;

    while (stud[i].length < answers.length) {
      pattern[i].forEach((item) => {
        stud[i].push(item);
      });
    }

    for (let j = 0; j < answers.length; j++) {
      if (stud[i][j] == answers[j]) {
        cnt++;
      }
    }

    if (cnt > curMax) {
      answer = [i];
      curMax = cnt;
    } else if (cnt == curMax) {
      answer.push(i);
    } else {
      continue;
    }
  }

  if (answer.length > 1) {
    answer.sort();
  }

  return answer;
}

JSON.stringify(solution(answers)) == JSON.stringify(expectedAnswer)
  ? console.log("The answer is correct")
  : console.log(
      `Wrong answer: ${solution(answers)}\nExpected Answer: ${expectedAnswer}`
    );
