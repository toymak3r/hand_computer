int media(int *valores){
  int result = 0;
  for (int i = 0; i < 10; i++){
    result = result + valores[i];
  };
  return result/10;
}

