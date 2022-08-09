import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		try {
			int num = Integer.parseInt(br.readLine());
			for(int i=0; i<num; i++) {
				String text = br.readLine();
				String eachNum[] = text.split(" ");
				int a = Integer.parseInt(eachNum[0]);
				int b = Integer.parseInt(eachNum[1]);
				bw.write(a+b + "\n");
			}
            bw.flush();
		} catch(NumberFormatException e) {
			e.printStackTrace();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
}
