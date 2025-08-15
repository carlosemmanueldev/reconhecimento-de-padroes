class Q3 {
  public static void main(String[] args) {
    int[][] img1 = ImagemDigital.carregarImagem("Fig0229(a).png");
    int[][] img2 = ImagemDigital.carregarImagem("Fig0229(b).png");
    int[][] result = null;
    result = new int[img1.length][img1[0].length];
    
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = (int) (((float)img1[i][j] / (float)img2[i][j]) * 255F);
      }
    }
  
    ImagemDigital.plotarImagem(result, "Divisão");
  }
}