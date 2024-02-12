/**
 *
 * Day1.java
 * Author: RM
 *
 */
import java.io.*;
import java.util.regex.*;

public class Day1 {

    public static void main(String[] args) {
        
        BufferedReader reader;
        String inFileName = System.getProperty(("user.dir")) + "\\day1\\day1.txt";
        //String inFileName = System.getProperty(("user.dir")) + "\\day1\\day1-practice.txt";
        try{
            reader = new BufferedReader(new FileReader(inFileName));
			String line = reader.readLine();

            Pattern pattern;
            pattern = Pattern.compile("[0-9]");
            Matcher matcher;
            boolean first_cap = false;
            String first_numeral = "";
            String last_numeral = "";

            Integer total_sum = 0;
			while (line != null) {
				System.out.println(line);

                for (String i : line.split("")) {
                    matcher = pattern.matcher(i);
                    if (matcher.find()) {
                        System.out.println(i);
                        if (!first_cap) {
                            first_numeral = i;
                            first_cap = true;
                        } 
                        last_numeral = i;
                    }
                }
                first_cap = false;
                System.out.printf("Number is: %s%s\n", first_numeral, last_numeral);
                total_sum = total_sum + Integer.parseInt(first_numeral+last_numeral);
				line = reader.readLine();
			}
            System.out.printf("Total sum: %d\n", total_sum);
            

			reader.close();

        }catch(Exception ex){
            ex.printStackTrace();
        }
    }
}