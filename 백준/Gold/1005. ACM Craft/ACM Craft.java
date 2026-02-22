import java.util.*;
import java.io.*;
public class Main {
    static int E;
    static int V;
    static int[] cost;
    static ArrayList<Integer>[] graph;
    public static void main(String args[]) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(bufferedReader.readLine());
        for(int tc=0; tc<T; tc++){
            st = new StringTokenizer(bufferedReader.readLine());
            E = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());
            cost = new int[E+1];

            st = new StringTokenizer(bufferedReader.readLine());
            for(int i=1; i<=E; i++){
                cost[i] = Integer.parseInt(st.nextToken());
            }
            graph = new ArrayList[E+1];
            for(int i=0; i<=E; i++){
                graph[i] = new ArrayList<Integer>();
            }
            int[] counter = new int[E+1];
            boolean[] starter = new boolean[E+1];
            for(int i=1; i<=V; i++){
                st = new StringTokenizer(bufferedReader.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                starter[end] = true;
                counter[end] += 1;
                graph[start].add(end);
            }
            int goal = Integer.parseInt(bufferedReader.readLine());
            int answer = Integer.MAX_VALUE;

            int[] checker = new int[E+1];
            for(int j=0; j<=E; j++){
                checker[j] = cost[j];
            }

            ArrayDeque<Integer> q = new ArrayDeque<>();

            for(int i=1; i<=E; i++){
                if(!starter[i]){
                    q.offerLast(i);
                }
            }

            while (!q.isEmpty()){
                int current = q.pollFirst();

                for(int i=0; i<graph[current].size(); i++){
                    int nextNode = graph[current].get(i);

                   checker[nextNode] = Math.max(checker[nextNode], checker[current] + cost[nextNode]);

                    counter[nextNode] -= 1;

                    if(counter[nextNode] == 0){
                        q.offerLast(nextNode);
                    }
                }
            }

            answer = checker[goal];
            System.out.println(answer);
        }
    }
}
