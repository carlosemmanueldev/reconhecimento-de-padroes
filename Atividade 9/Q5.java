class Q5 {
  public static void main(String[] args) {
    int[][] img1 = ImagemDigital.carregarImagem("ruido/lena1.png");
    int n = 100;
      
    for (int k = 2; k < n; k++) {
      int[][] img2 = ImagemDigital.carregarImagem("ruido/lena"+k+".png");
      
      for (int i = 0; i < img1.length; i++) {
        for (int j = 0; j < img1[i].length; j++) {
          img1[i][j] = img1[i][j] + img2[i][j];
        }
      }
    }

    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        img1[i][j] = img1[i][j] / n;
      }
    }
    
    ImagemDigital.plotarImagem(img1, "Média");
  }
}