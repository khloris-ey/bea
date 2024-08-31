import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;



import java.io.*;
import org.json.simple.JSONObject;




public class bankjava {public static void main(String[] args)throws IOException{
   System.out.println("BANK");
   Bank bank= new Bank("BBBB ", "Manila", "090909099", "1");
   bank.bank_info();

   Passbook pb = new Passbook("1000", "Joint Account", "0001", "Beatrice", "Sanchez","Dela Cruz", "00022", "01-01-01", 10000.00, 4000.00, 1000000.00);
   System.out.println(pb.display_passbook());

//    Savings si= new Savings(1000, 0001, "122345", "bea", "sanchez", "dela cruz", "female", "july 15, 2024", "filipino","bulacan", "8098094");
//    si.displayAccountInfo();
//    si.displaySavings();

   UI ui= new UI();
   ui.home();
    

}
    
}

class UI{

    public void home() throws IOException{
        BufferedReader bfn= new BufferedReader(new InputStreamReader(System.in));
        
        System.out.println("WELCOME TO BBB BANK");

        System.out.println("1. Create Account \n 2.Log In \n 3.Exit");

        System.out.print("Choice: ");
        String choice= bfn.readLine();
        if (choice.equalsIgnoreCase("1")){
            System.out.println("1.Saving Account \n 2.Checking Account \n 3.Joint Account");
            System.out.print("Choice: ");
            String c= bfn.readLine();

            if(c.equalsIgnoreCase("1")){
                Savings_Interface si= new Savings_Interface();
                si.create_savings();
            }
            if (c.equalsIgnoreCase("2")){
                Checking_Interface ci= new Checking_Interface();
                ci.create_checking();
            }

        }

        if (choice.equalsIgnoreCase("2")){
            System.out.println("1. Savings Account \n2. Checking Account\n3. Joint Account \n4. Exit");
            System.out.print("Choice: ");
            String ch= bfn.readLine();

            if (ch.equalsIgnoreCase("1")){
                Savings_Interface si2= new Savings_Interface();
                si2.create_login();
            }
            if (ch.equalsIgnoreCase("2")){
                Checking_Interface ci2= new Checking_Interface();
            }
        }
    }
    






}

class Bank{
    private String bankname;
    private String banklocation;
    private String branch_num;
    private String contact;
    

    public Bank(String name, String location, String contact, String branch_num){
        this.bankname= name;
        this.banklocation= location;
        this.branch_num= branch_num;
        this.contact= contact;
        
    }

    public void set_bankname(String bank_name){
        this.bankname= bank_name;
    }

    public void set_contact(String c){
        this.contact= c;
    }

    public void bank_info(){
        System.out.print("Bank: " + bankname + " ");
        System.out.print("Bank Location: " + banklocation + " ");
        System.out.print("Branch Number: " + branch_num + " ");
        System.out.print("Contact: " + contact+ " ");
    }
}

class Passbook{
    private String acc_type;
    private String acc_num;
    private String fname;
    private String mname;
    private String lname;
    private String fullname;
    private String passbooknum;
    private String transaction_number;
    private String transaction_date;
    private Double withdrawal;
    private Double deposit;
    private Double balance;

    public Passbook(String passbooknum,String acctype, String accnum, String fname, String mname, String lname, String transactionnum, String transaction_date,Double deposit, Double withdraw, Double balance ){
        this.passbooknum=passbooknum;
        this.acc_type=acctype;
        this.acc_num=accnum;
        this.fname= fname;
        this.mname= mname;
        this.lname= lname;
        this.fullname= lname + fname + mname;
        this.transaction_number= transactionnum;
        this.transaction_date= transaction_date;
        this.deposit= deposit;
        this.withdrawal=withdraw;
        this.balance= balance;
    }

    public String display_passbook(){
        String passbook = String.format("Passbook---Passbook No. %s----Transaction Code: %s \n Account Type: %s--Transaction Date: %s--Account Number: %s-- Full name: %s--Credited Amount: %.2f-- Debited Amount: %.2f-- Balance: %.2f",
                this.passbooknum, this.transaction_number, this.acc_type, this.transaction_date, 
                this.acc_num, this.fullname, 
                this.withdrawal, this.deposit, this.balance);
        return passbook;
    }

}


class Savings {
    private String ddate;
    private Integer user_id;
    private Integer acc_num;
    private String password;
    private String fname;
    private String mname;
    private String lname;
    private String gender;
    private String bdate;
    private String nationality;
    private String address;
    private String contact;
    protected static Map <Integer, Map<String, String>> savings;
    private Double withdraw;
    private Double deposit;
    private Double balance;
    private Double deposited;
    private Double credited;
    private Double debited;

    public Savings(Integer accnum, Integer user_id, String pass_word, String f_name, String m_name, String l_name, String gender, String bdate, String nationality, String address, String contact) {
        this.ddate = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy/dd/MM HH:mm:ss"));
        this.acc_num = accnum;
        this.user_id = user_id;
        this.password = pass_word;
        this.fname = f_name;
        this.mname = m_name;
        this.lname = l_name;
        this.gender = gender;
        this.bdate = bdate;
        this.nationality = nationality;
        this.address = address;
        this.contact = contact;
        this.savings = new HashMap<>();
        this.balance = 0.0;
        this.withdraw = 0.0;
        this.deposited = 0.0;
        this.debited= 0.0;
        this.credited=0.0;
        initSavings();
    }

    public  Double debit(Double amount){
        this.withdraw= amount;
        this.debited+=this.withdraw;
        Double new_bal= this.balance-this.debited;
        this.balance= new_bal; 
        this.withdraw=0.0;

        System.out.println("New Balance after debit: " + this.balance);
        return this.balance;

        // Savings instance= getSavingsInstance();
        // instance.withdraw= amount;
        // instance.debited+=instance.withdraw;
        // Double new_bal= instance.balance- instance.debited;
        // instance.balance-= new_bal;
        
        // System.out.println(instance.balance);
        // return instance.balance;


    }

    public Double credit(Double amount) {
        // if (amount <= 0) {
        //     System.out.println("Invalid amount. The amount to be credited should be greater than 0.");
        //     return this.balance;
        // }

        this.deposited = amount;
        this.credited += this.deposited;
        this.balance += this.deposited;
        this.deposited = 0.0; // Reset deposited amount after addition

        System.out.println("New Balance after credit: " + this.balance);
        return this.balance;
    }
    private static Savings getSavingsInstance() {
        // This method returns an instance of Savings. Modify this method to return
        // the actual instance you are working with.
        return new Savings(0, 0, "", "", "", "", "", "", "", "", "");
    }


    private void initSavings() {
        Map<String, String> accountDetails = new HashMap<>();
        accountDetails.put("Date and Time", this.ddate);
        accountDetails.put("Username", this.fname + " " + this.mname + " " + this.lname);
        accountDetails.put("Password", this.password); // Store the actual password
        accountDetails.put("Contact", this.contact);
        this.savings.put(this.acc_num, accountDetails);
    }

    public void addSavingsAccount(Integer accnum, String dateTime, String username, String password, String contact) {
        Map<String, String> accountDetails = new HashMap<>();
        accountDetails.put("Date and Time", dateTime);
        accountDetails.put("Username", username);
        accountDetails.put("Password", password);
        accountDetails.put("Contact", contact);
        this.savings.put(accnum, accountDetails);
    }

    public void displayAccountInfo() {
        System.out.println("Account Number: " + this.acc_num);
        System.out.println("User ID: " + this.user_id);
        System.out.println("Name: " + this.fname + " " + this.mname + " " + this.lname);
    }

    public void displaySavings() {
        for (Map.Entry<Integer, Map<String, String>> entry : savings.entrySet()) {
            System.out.println("Account Number: " + entry.getKey());
            for (Map.Entry<String, String> details : entry.getValue().entrySet()) {
                System.out.println(details.getKey() + ": " + details.getValue());
            }
        }
        System.out.println(savings);
    }

    public String toJSON() {
        JSONObject json = new JSONObject();
        for (Map.Entry<Integer, Map<String, String>> entry : savings.entrySet()) {
            json.put("Account Number", entry.getKey());
            Map<String, String> details = entry.getValue();
            JSONObject accountDetails = new JSONObject();
            for (Map.Entry<String, String> detail : details.entrySet()) {
                accountDetails.put(detail.getKey(), detail.getValue());
            }
            json.put("Details", accountDetails);
        }
        return json.toJSONString();
    }
}

class Savings_Interface  { 

    // public Savings_Interface(Integer accnum, Integer user_id, String pass_word, String f_name, String m_name,
    //         String l_name, String gender, String bdate, String nationality, String address, String contact) {
    //     super(accnum, user_id, pass_word, f_name, m_name, l_name, gender, bdate, nationality, address, contact);
        
    // }

    private Savings currentAcc;

    public void create_savings() throws IOException{
    BufferedReader bfn = new BufferedReader(new InputStreamReader(System.in));
    Integer savingsaccnum= 1000;
    Integer savinguserid=00000;
    System.out.println("CREATE SAVINGS ACCOUNT");
    System.out.print("First Name: ");
    String fname= bfn.readLine();

    System.out.print("Middle Name: ");
    String mname= bfn.readLine();
    
    System.out.print("Last Name: ");
    String lname= bfn.readLine();

    System.out.print("Gender: ");
    String gender= bfn.readLine();

    System.out.print("Nationality: ");
    String nationality= bfn.readLine();

    System.out.print("Contact: ");
    String contact= bfn.readLine();

    System.out.print("Birthday: ");
    String bday= bfn.readLine();

    System.out.print("Address: ");
    String address=  bfn.readLine();

    System.out.print("Confirm the following?");
    String confirm= bfn.readLine();

    System.out.print("Password?");
    String pw= bfn.readLine();

    if (confirm.equalsIgnoreCase("yes")){
        savingsaccnum+=1;
        savinguserid+=1;
    }

    currentAcc= new Savings(savingsaccnum, savinguserid, pw, fname, mname, lname, gender, bday, nationality, address, contact);
    currentAcc.displayAccountInfo();
    currentAcc.displaySavings();

    String savingsJson= currentAcc.toJSON();
    System.out.println("Savings JSON:");
    System.out.println(savingsJSON);

    create_login();

}   

    public void create_login() throws IOException{
        BufferedReader bfn= new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter Username: ");
        String username= bfn.readLine();

        System.out.print("Enter Password: ");
        String pw= bfn.readLine();

        boolean loginsuccess= false;

        for (Map.Entry<Integer,Map<String, String>> entry: Savings.savings.entrySet()){
            Map<String, String> accountInfo = entry.getValue();
            if (accountInfo.get("Username").equals(username) && accountInfo.get("Password").equals(pw)) {
                System.out.println("Login successful!");
                savings_transaction();
                loginsuccess = true;
                break;
        }


    }
        if (!loginsuccess) {
            System.out.println("Invalid username or password. Please try again.");
           
        }
            
        
    }

    public void savings_transaction() throws IOException{
        BufferedReader bfn = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("SAVING TRANSACTION MENU");
        System.out.println(" ");
        System.out.println("1. Deposit \n2. Withdraw \n3. Check Account \n4. Exit");
        System.out.println(" ");
        System.out.print("Choice: ");
        String choice= bfn.readLine();

        if (choice.equalsIgnoreCase("1")){

            System.out.print("Amount to deposit: ");
            Double amt= Double.parseDouble(bfn.readLine());

            currentAcc.credit(amt);

            savings_transaction();
            
        }

        else if (choice.equalsIgnoreCase("2")){
            System.out.print("Amount to withdraw: ");
            Double amt= Double.parseDouble(bfn.readLine());

            currentAcc.debit(amt);
            savings_transaction();

        }

        



        

    }
}


class Checking{
    private String ddate;
    private Integer user_id;
    private Integer acc_num;
    private String password;
    private String fname;
    private String mname;
    private String lname;
    private String gender;
    private String bdate;
    private String nationality;
    private String address;
    private String contact;
    protected static Map <Integer, Map<String, String>> checking;
    private Double withdraw;
    private Double deposit;
    private Double balance;
    private Double deposited;
    private Double credited;
    private Double debited;

    public Checking(Integer accnum, Integer user_id, String pass_word, String f_name, String m_name, String l_name, String gender, String bdate, String nationality, String address, String contact) {
        this.ddate = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy/dd/MM HH:mm:ss"));
        this.acc_num = accnum;
        this.user_id = user_id;
        this.password = pass_word;
        this.fname = f_name;
        this.mname = m_name;
        this.lname = l_name;
        this.gender = gender;
        this.bdate = bdate;
        this.nationality = nationality;
        this.address = address;
        this.contact = contact;
        this.checking = new HashMap<>();
        this.balance = 0.0;
        this.withdraw = 0.0;
        this.deposited = 0.0;
        this.debited= 0.0;
        this.credited=0.0;
        initSavings();
    }

    private void debit(){
        this.debited+=this.withdraw;
        Double new_bal= this.balance-this.debited;
        this.balance= new_bal; 
        this.withdraw=0.0;

    }

    private void credit(){
        this.credited+=this.deposited;
        Double bal_new= this.balance+ this.credited;
        this.balance+=bal_new;
        this.deposit=0.0;
    }


    private void initSavings() {
        Map<String, String> accountDetails = new HashMap<>();
        accountDetails.put("Date and Time", this.ddate);
        accountDetails.put("Username", this.fname + " " + this.mname + " " + this.lname);
        accountDetails.put("Password", this.password); // Store the actual password
        accountDetails.put("Contact", this.contact);
        this.checking.put(this.acc_num, accountDetails);
    }

    public void addCheckingAccount(Integer accnum, String dateTime, String username, String password, String contact) {
        Map<String, String> accountDetails = new HashMap<>();
        accountDetails.put("Date and Time", dateTime);
        accountDetails.put("Username", username);
        accountDetails.put("Password", password);
        accountDetails.put("Contact", contact);
        this.checking.put(accnum, accountDetails);
    }

    public void displayAccountInfo() {
        System.out.println("Account Number: " + this.acc_num);
        System.out.println("User ID: " + this.user_id);
        System.out.println("Name: " + this.fname + " " + this.mname + " " + this.lname);
    }

    public void displayChecking() {
        for (Map.Entry<Integer, Map<String, String>> entry : checking.entrySet()) {
            System.out.println("Account Number: " + entry.getKey());
            for (Map.Entry<String, String> details : entry.getValue().entrySet()) {
                System.out.println(details.getKey() + ": " + details.getValue());
            }
        }
        System.out.println(checking);
    }
    
    
}

class Checking_Interface{
    
    public void create_checking() throws IOException{
        BufferedReader bfn = new BufferedReader(new InputStreamReader(System.in));
        Integer checkingaccnum= 2000;
        Integer checkinguserid=00000;
        System.out.println("CREATE SAVINGS ACCOUNT");
        System.out.print("First Name: ");
        String fname= bfn.readLine();
    
        System.out.print("Middle Name: ");
        String mname= bfn.readLine();
        
        System.out.print("Last Name: ");
        String lname= bfn.readLine();
    
        System.out.print("Gender: ");
        String gender= bfn.readLine();
    
        System.out.print("Nationality: ");
        String nationality= bfn.readLine();
    
        System.out.print("Contact: ");
        String contact= bfn.readLine();
    
        System.out.print("Birthday: ");
        String bday= bfn.readLine();
    
        System.out.print("Address: ");
        String address=  bfn.readLine();
    
        System.out.print("Confirm the following?");
        String confirm= bfn.readLine();
    
        System.out.print("Password?");
        String pw= bfn.readLine();
    
        if (confirm.equalsIgnoreCase("yes")){
            checkingaccnum+=1;
            checkinguserid+=1;
        }
        Checking check = new Checking(checkingaccnum, checkinguserid, pw, fname, mname, lname, gender, bday, nationality, address, contact);
        check.displayAccountInfo();
        check.displayChecking();

        create_login();

    
    
}
    public void create_login() throws IOException{
        BufferedReader bfn= new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter Username: ");
        String username= bfn.readLine();

        System.out.print("Enter Password: ");
        String pw= bfn.readLine();

        boolean loginsuccess= false;

        for (Map.Entry<Integer,Map<String, String>> entry: Checking.checking.entrySet()){
            Map<String, String> accountInfo = entry.getValue();
            if (accountInfo.get("Username").equals(username) && accountInfo.get("Password").equals(pw)) {
                System.out.println("Login successful!");
                // Perform transactions or further actions
                loginsuccess = true;
                break;
        }


    }
        if (!loginsuccess) {
            System.out.println("Invalid username or password. Please try again.");}
    }
}
