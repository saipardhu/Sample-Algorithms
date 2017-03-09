
public class TowersofHanoi {
	public static void main(String[] args){
        int disks=64;  //given the number of disks as 64
        TowersofHanoi t = new TowersofHanoi();
        t.TOI(64,"Pole1","Pole2","Pole3");
    }
    public void TOI(int n, String A_pole, String B_pole, String C_pole){
        if(n==1) System.out.println(A_pole +"shifted to" + B_pole);
        else{
            TOI(n-1,A_pole,C_pole,B_pole);   
            System.out.println(A_pole +" "+" shifted to "+" "+ B_pole);
            TOI(n-1,B_pole,A_pole,C_pole);
        }
        
    }

}
