import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // the total number of nodes in the level, including the gateways
        int L = in.nextInt(); // the number of links
        int E = in.nextInt(); // the number of exit gateways
        
        int[][] links = new int[L][2]; // [total number of links][N1 and N2] 
        int[][] gatewayLinks = new int[100][2]; // [just a big number][immediate child of gateway(node) and index of pair in links]

        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt(); // N1 and N2 defines a link between these nodes
            int N2 = in.nextInt();
            links[i][0] = N1;
            links[i][1] = N2;
        }
        
        int counter = 0;
        for (int i = 0; i < E; i++) {
            int EI = in.nextInt(); // the index of a gateway node

            for(int j = 0; j < L; j++) {
                if(links[j][0] == EI) {
                    gatewayLinks[counter][0] = links[j][1]; //node
                    gatewayLinks[counter][1] = j; // index
                    counter++;
                }
                if(links[j][1] == EI) {
                    gatewayLinks[counter][0] = links[j][0]; // node
                    gatewayLinks[counter][1] = j; // index
                    counter++;
                }
            }
        }

        for(int bar = 0; bar < counter; bar++) {
            System.err.println(gatewayLinks[bar][0] + " " + gatewayLinks[bar][1]);
        }

        // game loop
        while (true) {
            String linkToCut = "";
            boolean far = true; int c = 0;
            int SI = in.nextInt(); // The index of the node on which the Bobnet agent is positioned this turn
            for(int m = 0; m <= counter; m++) {
                if(gatewayLinks[m][0] == SI) {
                    int index = gatewayLinks[m][1];
                    linkToCut = links[index][0] + " " + links[index][1];
                    far = false;
                }
            }
            if(far) {
                int foo = gatewayLinks[c][1];
                linkToCut = links[foo][0] + " " + links[foo][1];
                c++;
            }
            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");


            // Example: 0 1 are the indices of the nodes you wish to sever the link between
            System.out.println(linkToCut);
        }
    }
}