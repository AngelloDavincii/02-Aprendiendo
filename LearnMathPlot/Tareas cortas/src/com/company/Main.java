package com.company;

import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) {
        PriorityQueue<String> pQueue = new PriorityQueue<String>();

        pQueue.add("Ramon");
        pQueue.add("Juanes");
        pQueue.add("Pedro");
        pQueue.add("Paul");
        pQueue.add("Andrea");
        pQueue.add("Arquimedes");
        pQueue.add("Jarod");
        pQueue.add("Daniela");
        pQueue.add("Juanito");

        System.out.println("Head : " + pQueue.peek());
        System.out.println("Head : " + pQueue.element() + "\n");

        while(pQueue.isEmpty()){
            System.out.println(pQueue.poll() + " ");

        }
        System.out.println("\n");
        pQueue.add("Ramon");
        pQueue.offer("Juanes");
        pQueue.add("Pedro");
        pQueue.offer("Paul");
        pQueue.add("Andrea");
        pQueue.offer("Arquimedes");
        pQueue.add("Jarod");
        pQueue.offer("Daniela");
        pQueue.add("Juanito");

        while(pQueue.isEmpty()){
            System.out.println(pQueue);
            System.out.println("Removed : " + pQueue.remove());
            System.out.println(pQueue);
            System.out.println("");

        }

    }

}
