class Q4 {
  public static void main(String[] args) {
    int[][] img1 = ImagemDigital.carregarImagem("Fig0230(a).png");
    int[][] img2 = ImagemDigital.carregarImagem("Fig0230(b).png");
    int[][] result = null;
    result = new int[img1.length][img1[0].length];
    
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = ((img1[i][j] * img2[i][j]) / 255);
      }
    }
  
    ImagemDigital.plotarImagem(result, "Multiplicação");
  }
}