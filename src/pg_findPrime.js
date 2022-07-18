numbers = "17";
expectedAnswer = 3;

const getPermutations = function (arr, numberSelect) {
  const result = [];
  if (numberSelect === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, numberSelect - 1);
    const permutation = permutations.map((p) => [fixed, ...p]);
    result.push(...permutation);
  });

  return result;
};

const isPrime = function (n) {
  if (n === 0 || n === 1) return false;

  for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

function solution(numbers) {
  let answer = 0;

  const nArr = numbers.split("");
  let ansArr = [];

  // 1부터 nArr의 길이 만큼 반복하며, 순열 도출
  for (let i = 1; i <= nArr.length; i++) {
    let pArr = getPermutations(nArr, i);

    // 도출한 순열을 Number로 바꾸어 결과 배열에 추가
    pArr.forEach((el) => {
      const num = Number(el.toString().replace(/,/g, ""));
      ansArr.push(num);
    });
  }

  // 중복 제거
  const setArr = new Set(ansArr);
  ansArr = [...setArr];

  // 소수 판별
  ansArr.forEach((el) => {
    if (isPrime(el)) {
      answer++;
    }
  });

  return answer;
}

JSON.stringify(solution(numbers)) == JSON.stringify(expectedAnswer)
  ? console.log("The answer is correct")
  : console.log(
      `Wrong answer: ${solution(numbers)}\nExpected Answer: ${expectedAnswer}`
    );
