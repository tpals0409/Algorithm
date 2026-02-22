import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

/*
모든 토마토 개수 기억.
전부 되면 출력, 안되면 -1
 */
public class Main{
    static int M;
    static int N;
    static int H;
    static int counter;
    static boolean[][][] visited;
    static int[][][] tomato;
    static int totalTomato;
    static int answer;

    static int[] dh = {0, 0, 0, 0, 1, -1};
    static int[] dy = {1, 0, -1, 0, 0, 0};
    static int[] dx = {0, 1, 0, -1, 0, 0};
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        M = Integer.parseInt(stringTokenizer.nextToken());
        N = Integer.parseInt(stringTokenizer.nextToken());
        H = Integer.parseInt(stringTokenizer.nextToken());
        counter = 0;
        totalTomato = H*M*N;
        visited = new boolean[H][N][M];
        tomato = new int[H][N][M];
        answer = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();


        for(int box=0; box<H; box++){
            for(int y=0; y<N; y++){
                stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                for(int x=0; x<M; x++){
                    int tmp = Integer.parseInt(stringTokenizer.nextToken());
                    tomato[box][y][x] = tmp;
                    if(tmp==1){
                        visited[box][y][x] = true;
                        counter += 1;
                        q.offerLast(new int[] {box, y, x, 0});
                    }
                    if(tmp== -1){
                        visited[box][y][x] = true;
                        totalTomato -= 1;
                    }
                }
            }
        }
        while(!q.isEmpty()){
            int[] tmp = q.pollFirst();
            for(int i=0; i<6; i++){
                int nh = tmp[0]+dh[i];
                int ny = tmp[1]+dy[i];
                int nx = tmp[2]+dx[i];


                if((nh>=0 && nh<H) && (ny>=0 && ny<N) && (nx>=0 && nx<M) && !visited[nh][ny][nx]){
                    visited[nh][ny][nx] = true;
                    counter += 1;
                    answer = Math.max(answer, tmp[3]+1);
                    q.offerLast(new int[] {nh, ny, nx, tmp[3]+1});
                }
            }
        }
        if(counter == totalTomato){
            System.out.println(answer);
        }
        else{
            System.out.println(-1);
        }
    }
}