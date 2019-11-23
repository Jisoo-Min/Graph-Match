class Logic2Closefar{ 
/* Given three ints, a b c, return true if one of b or c is "close" 
 * (differing from a by at most 1), while the other is "far", differing from 
 * both other values by 2 or more. Note: Math.abs(num) computes the absolute 
 * value of a number.
 */
public boolean closeFar(int a, int b, int c) {
    if(isClose(a, b) && isFar(a, b, c)) || (isClose(a, c) && isFar(a, c, b)){
        return true;
    }else{
        return false;
    }
}

public boolean isClose(int a, int b) {
    if(Math.abs(a - b) <= 1){
        return true;
    }else{
        return false;
    }
}

public boolean isFar(int a, int b, int c) {
    if(Math.abs(a - c) >= 2 && Math.abs(b - c) >= 2){
        return true;
    }else{
        return false;
    }
    
}
}
