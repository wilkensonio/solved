package com.company;
// https://leetcode.com/problems/coin-change/submissions/952121452/

public class Main {

    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.print(coinChange( coins, amount));
    }

    public static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            dp[i] = amount + 1;
            for (int coin : coins) {
                if (coin <= i){
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount]== amount + 1 ? -1 : dp[amount];
    }
}
