double dot(int n, double *a, int m, double *b){
  double sum = 0.0;
  for (int i=0; i<n; i++){
    sum += a[i]*b[i];
  }
  return sum;
}

void create_list(int size, double *arr){
  for (int i=0; i<size; i++)
    arr[i] = i;
}
