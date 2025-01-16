import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class PenetrationToolkit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the Penetration Testing Toolkit");
        System.out.println("1. Port Scanner");
        System.out.println("2. Brute Forcer");
        System.out.print("Enter your choice: ");
        
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        switch (choice) {
            case 1:
                runPortScanner(scanner);
                break;
            case 2:
                runBruteForcer(scanner);
                break;
            default:
                System.out.println("Invalid choice. Exiting...");
        }
    }

    // Port Scanner Module
    private static void runPortScanner(Scanner scanner) {
        System.out.print("Enter the target IP: ");
        String targetIp = scanner.nextLine();

        System.out.print("Enter the start port: ");
        int startPort = scanner.nextInt();

        System.out.print("Enter the end port: ");
        int endPort = scanner.nextInt();

        System.out.println("Scanning ports on " + targetIp + "...");
        ExecutorService executor = Executors.newFixedThreadPool(10);

        for (int port = startPort; port <= endPort; port++) {
            int currentPort = port;
            executor.execute(() -> {
                try (Socket socket = new Socket()) {
                    socket.connect(new InetSocketAddress(targetIp, currentPort), 200);
                    System.out.println("Port " + currentPort + " is open.");
                } catch (IOException ignored) {
                    // Port is closed or unreachable
                }
            });
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
            // Wait for all tasks to finish
        }

        System.out.println("Port scan completed.");
    }

    // Brute Forcer Module
    private static void runBruteForcer(Scanner scanner) {
        System.out.print("Enter the target IP: ");
        String targetIp = scanner.nextLine();

        System.out.print("Enter the target port: ");
        int targetPort = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        System.out.print("Enter the username: ");
        String username = scanner.nextLine();

        System.out.print("Enter the path to the password file: ");
        String passwordFile = scanner.nextLine();

        System.out.println("Starting brute force attack on " + targetIp + ":" + targetPort);

        try (BufferedReader br = new BufferedReader(new FileReader(passwordFile))) {
            String password;
            while ((password = br.readLine()) != null) {
                if (tryLogin(targetIp, targetPort, username, password)) {
                    System.out.println("Login successful with password: " + password);
                    return;
                } else {
                    System.out.println("Attempt failed with password: " + password);
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading password file: " + e.getMessage());
        }

        System.out.println("Brute force attack completed. No valid credentials found.");
    }

    private static boolean tryLogin(String targetIp, int targetPort, String username, String password) {
        // Simulated login function (replace with actual implementation for real protocols)
        // This function always returns false for demonstration purposes.
        return false;
    }
}



