public class tracker1{

    
    static int[] repeats = new int[111]; 
    static int maxrepeats = 0;
    static Integer mode;

  
    static int totalNumbers = 0;
    static double totalSum = 0.0;
    static Double mean;


    static Integer mintemperature;
    static Integer maxtemperature;

    public static void insert(int t) {


        repeats[t]++;
        if (repeats[t] > maxrepeats) {
            mode = t;
            maxrepeats = repeats[t];
        }

        totalNumbers++;
        totalSum += t;
        mean = totalSum / totalNumbers;
        if (maxtemperature == null || t > maxtemperature) {
            maxtemperature = t;
        }
        if (mintemperature == null || t < mintemperature) {
            mintemperature = t;
        }
    }


    public static Integer getMax() {
        return maxtemperature;

    }


    public static Integer getMin() {
        return mintemperature;

    }


    public static Double getMean() {
        return mean;

    }


    public static Integer getMode() {
        return mode;

    }


    public static void main(String[] args) {
    	


    	insert(50);
    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(80);

    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(80);

    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());


    	insert(30);
        
    	System.out.println("max "+getMax()+" min"+getMin()+" mean "+getMean()+" mode "+getMode());



    }
}

