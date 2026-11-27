'use strict';

function contentText(value, x, y, opacity, opts = {}) {
  txt(value, x, y, { size: 50, fam: F.mono, align: 'center', c: C.white, a: opacity, ...opts });
}

function contentTitle(value, opacity) {
  contentText(value, W / 2, 190, opacity, { size: 64, fam: F.disp, c: C.cyan });
}

SCENES.row = scene => {
  const heading = at(scene, 0, 0.4, -0.4);
  const gcd = at(scene, 1, 0.45);
  const witness = at(scene, 2, 0.45);
  contentTitle('What divides the whole row?', heading);
  ['4', '−14', '10', '6'].forEach((coefficient, index) => {
    const x = 380 + index * 325;
    chip(x, 310, 185, 125, coefficient, C.cyan, heading, 66);
    contentText('÷ 2', x + 92, 505, gcd, { size: 40, c: C.now });
  });
  contentText('row 3: gcd = 2', W / 2, 620, gcd);
  contentText('row 8: gcd = 1  ≠  divisor count 2', W / 2, 765, witness, { size: 45, c: C.now });
};

SCENES.bridge = scene => {
  const samples = at(scene, 0, 0.45, -0.25);
  const arrows = at(scene, 1, 0.5);
  const conclusion = at(scene, 2, 0.45);
  contentTitle('Change the list, keep the gcd', samples);
  panel(200, 325, 610, 280, samples, C.cyan, 'COEFFICIENTS');
  panel(1110, 325, 610, 280, samples, C.cyan, 'SAMPLES AT POSITIVE INTEGERS');
  contentText('a(n,0), …, a(n,n)', 505, 500, samples, { size: 37 });
  contentText('Bₙ(1), Bₙ(2), Bₙ(3), …', 1415, 500, samples, { size: 37 });
  contentText('⇄', W / 2, 505, arrows, { size: 95, c: C.now });
  contentText('integer combinations in both directions', W / 2, 720, conclusion, { size: 45 });
};

SCENES.prime = scene => {
  const heading = at(scene, 0, 0.45, -0.25);
  const congruence = at(scene, 1, 0.5);
  contentTitle('An odd prime needs just one witness', heading);
  panel(250, 300, 1420, 260, congruence, C.cyan, 'CARLITZ CONGRUENCE');
  contentText('n = qp + r,   0 ≤ r < p', W / 2, 415, congruence, { size: 42 });
  contentText('Bₙ(x) ≡ x^(qp) Bᵣ(x)  mod p', W / 2, 510, congruence, { size: 51, fam: F.math });
  contentText('1     2     …     p−1', W / 2, 680, heading, { c: C.now });
  contentText('At least one nonzero remainder survives.', W / 2, 780, congruence, { size: 40 });
};

SCENES.two = scene => {
  const even = at(scene, 0, 0.45, -0.25);
  const odd = at(scene, 1, 0.45);
  const modFour = at(scene, 2, 0.45);
  contentTitle('Two is the only prime left', even);
  panel(180, 300, 740, 390, even, C.cyan, 'EVEN n ≥ 2');
  panel(1000, 300, 740, 390, odd, C.cyan, 'ODD n ≥ 3');
  contentText('Bₙ(1) is odd', 550, 500, even);
  contentText('Every sample is even', 1370, 465, odd, { size: 41 });
  contentText('Bₙ(3) ≡ 2  mod 4', 1370, 585, modFour, { c: C.now });
  contentText('No factor of two', 550, 778, even, { size: 42 });
  contentText('Exactly one factor of two', 1370, 778, modFour, { size: 42 });
};

SCENES.answer = scene => {
  const answer = at(scene, 0, 0.45, -0.25);
  const context = at(scene, 1, 0.45);
  contentTitle('Exact content of the row', answer);
  contentText('1  for 0, 1 and all even rows', W / 2, 380, answer, { size: 66 });
  contentText('2  for odd rows from 3 onward', W / 2, 520, answer, { size: 66 });
  contentText('A counterexample refutes a rule.', W / 2, 678, context, { size: 40, c: C.dim });
  contentText('Ma and Zhang prove the replacement.', W / 2, 758, context, { size: 40, c: C.argued });
};

FILM.poster = () => {
  box(0, 0, W, H, C.cyan, 1, 0, C.bg);
  contentText('COPELAND’S POLYNOMIAL ROWS', W / 2, 163, 1, { size: 43, c: C.cyan });
  contentText('WHY ONLY ONE OR TWO?', W / 2, 300, 1, { size: 91, fam: F.disp });
  contentText('系数的公因数为何只有一或二？', W / 2, 418, 1, { size: 58, fam: F.zh });
  ['4', '−14', '10', '6'].forEach((coefficient, index) => {
    chip(380 + index * 325, 535, 185, 142, coefficient, C.cyan, 1, 78);
  });
  contentText('ROW 3  •  GCD = 2', W / 2, 820, 1, { size: 60, c: C.now });
  contentText('Haobo Ma  ·  Wenlin Zhang  |  Version 2', W / 2, 965, 1, { size: 39, c: C.dim });
};
