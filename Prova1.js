mes = [
  "Janeiro", "Fevereiro", "Março"
];

meuAniversario = 3;

for (let i = 0; i < meuAniversario; i++) {
  if (i === meuAniversario - 1) {
    console.log(`Eu nasci em ${mes[i]}`);
  } else {
    console.log(mes[i]);
  }
}