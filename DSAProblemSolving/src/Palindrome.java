public class Palindrome {
    public static boolean isPalindrome(String s) {

        String ans = "";

        if (s == null || s.isEmpty()) {
            return true;
        }

        char[] arr = s.toCharArray();

        for (char c : arr) {
            System.out.println(c);
        }

        return true;




    }

    public static void main(String[] args) {

        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));


    }

}
