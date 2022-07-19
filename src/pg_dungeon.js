const getDungeons = function (arr, numSelect) {
  if (numSelect === 1) return arr.map((el) => [el]);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const dungeons = getDungeons(rest, numSelect - 1);
    const dungeon = dungeons.map((d) => [fixed, ...d]);

    result.push(...dungeon);
  });

  return result;
};

const searchD = function (arr, k) {
  let localK = k;
  let cnt = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i][0] <= localK) {
      // 방문할 수 있는 던전
      localK -= arr[i][1];
      cnt++;
    } else {
      break;
    }
  }
  return cnt;
};

function solution(k, dungeons) {
  let answer = 0;

  const _dungeons = getDungeons(dungeons, dungeons.length);

  for (let i = 0; i < _dungeons.length; i++) {
    const searchCnt = searchD(_dungeons[i], k);
    if (searchCnt > answer) {
      answer = searchCnt;
    }
  }

  return answer;
}

dungeons = [
  [80, 20],
  [50, 40],
  [30, 10],
];
expectedAnswer = 3;
k = 80;

JSON.stringify(solution(k, dungeons)) == JSON.stringify(expectedAnswer)
  ? console.log("The answer is correct")
  : console.log(
      `Wrong answer: ${solution(numbers)}\nExpected Answer: ${expectedAnswer}`
    );
