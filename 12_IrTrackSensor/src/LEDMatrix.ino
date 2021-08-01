//
///* Include DigitLedDisplay Library */
//#include "DigitLedDisplay.h"
///* Arduino Pin to Display Pin
//   11 to DIN,
//   10 to CS,
//   13 to CLK */
//DigitLedDisplay ld = DigitLedDisplay(11, 10, 13);
//
//void LEDMatrixInit(int Bright){
//    /* Set the brightness min:1, max:15 */
//  ld.setBright(Bright);
//
//  /* Set the digit count */
//  ld.setDigitLimit(8);
//}
//
//void disMatrix(int mat[8][8]){
//  int col,row,m_col,col_dat;
//  for(col=0;col<8;col++)
//  {
//    col_dat=0;
//    for(row=0;row<8;row++)
//    {
//      m_col=col+1;
//      col_dat+=mat[row][col]<<row;
//    }
//    ld.write(m_col, col_dat);
//  }
//}
