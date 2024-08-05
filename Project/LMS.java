import java.util.*;
public class LMS{
    //for registration
    class Rnode {
        String name;
        int roll;
        Rnode next;
        Rnode (String name, int roll){
            this.name = name;
            this.roll = roll;
            this.next = null;
        }
    }
    Rnode Rhead;
    //for enrolements
    class Enode {
        String subject;
        Enode next;
        Enode (String subject){
            this.subject = subject;
            this.next = null;
        }
    }
    Enode Ehead;
    //for list to BST
    class RTree {
        String name;
        int roll;
        RTree left,right;
        RTree (String name, int roll){
            this.name = name;
            this.roll = roll;
            this.left = null;
            this.right = null;
        }
    }
    //shows students registered in rlist
    void show(){

        if (Rhead==null){
            return;
        }
        System.out.println("--------------Currently Registered Students-------------");
        System.out.println("Sr Roll Names");
        Rnode current = Rhead ;
        int i=1;
        while (current!=null){
            System.out.print(i+":  "+ current.roll+"  "+current.name+"\n");
            current= current.next;
            i++;
        }
        
    }
    RTree RTroot;
    //addition in rlist
    Rnode addstud (String name , int roll) {
        Rnode temp = new Rnode(name, roll);
        if (Rhead == null){
            Rhead = temp;
        }
        else {
            temp.next = Rhead;
            Rhead = temp;
        }
        insertionSortList();
        return temp;
    }
    //deleting students in rlist
    Rnode delstud (int roll) {
        if (Rhead == null){
            return null;
        }
        else {
            if (Rhead.roll==roll){
                Rnode current = Rhead;
                Rhead = Rhead.next;
                return current;
            }
            Rnode current = Rhead;
            Rnode previous = null;
            while (current!=null){
                if (current.roll == roll){
                     previous.next = current.next;
                     //return current;
                }
                previous = current ;
                current = current.next;
            }
            return current;
        }
    }
    //sorting rlist
    void insertionSortList(){
        Rnode dummy = new Rnode(null,0);
        dummy.next = Rhead;
        Rnode prev = Rhead;
        Rnode current = Rhead.next;
        while (current!=null){
            if (current.roll>=prev.roll){
                prev = current;
                current = current.next;
                continue;
            }
            Rnode insert = dummy;
            while (current.roll > insert.next.roll){
                insert = insert.next;
            }
            prev.next = current.next;
            current.next = insert.next;
            insert.next = current;
            current = prev.next;
        }
        Rhead = dummy.next;
    }
    //
    ////shows students registered in rlist
    //void show(){
    //    if (Rhead==null){
    //        return;
    //    }
    //    Rnode current = Rhead ;
    //    while (current!=null){
    //        System.out.print(current.name+"->");
    //        current= current.next;
    //    }
    //    System.out.println("NULL");
    //}
    //search in rlist
    Rnode searchRnode (int roll){
        if (Rhead == null) {
            return null;
        }
        else {
            Rnode current = Rhead;
            while (current!=null) {
                if (current.roll==roll){
                    return current;
                }
                current = current.next;
            }
            return null;
        }
    }
    //addition in elist
    Enode addsub(String name){
        Enode temp = new Enode(name);
        if (Ehead == null){
            Ehead = temp;
        }
        else {
            temp.next = Ehead;
            Ehead = temp;
        }
        return Ehead;
    }
    //deletion in elist
    Enode delsub (String subject){
        if (Ehead == null){
            return null;
        }
        else {
            if (Ehead.subject==subject){
                Ehead = Ehead.next;
            }
            Enode current = Ehead;
            Enode previous = null;
            while (current!=null){
                if (current.subject == subject){
                     previous.next = current.next;
                }
                previous = current ;
                current = current.next;
            }
            return Ehead;
        }
    }
    //shows enrollments for each node in rlist
    void showsub(Enode head){
        if (head==null){
            return;
        }
        Enode current = head ;
        while (current!=null){
            System.out.print(current.subject+"->");
            current= current.next;
        }
        System.out.println("NULL");
    }
    
    public static void main(String[] args) {

        HashMap<Rnode,Enode> MAP = new HashMap<Rnode,Enode>();


        LMS Rlist = new LMS();
        Rnode rnode1 = Rlist.addstud("Abdullah", 28);
        LMS elist1 = new LMS();
        elist1.Ehead = elist1.addsub("DLD");
        elist1.Ehead = elist1.addsub("DSA");
        elist1.Ehead = elist1.addsub("CN");
        elist1.Ehead = elist1.delsub("DSA");
        MAP.put(rnode1, elist1.Ehead);
        Rnode rnode2 = Rlist.addstud("shiraz", 34);
        LMS elist2 = new LMS();
        MAP.put(rnode2, elist2.Ehead);
        Rnode rnode3 = Rlist.addstud("sher gull", 30);
        LMS elist3 = new LMS();
        MAP.put(rnode3, elist3.Ehead);
        Rnode rnode4 = Rlist.addstud("noman", 45);
        LMS elist4 = new LMS();
        elist4.Ehead = elist4.addsub("DLD");
        elist4.Ehead = elist4.addsub("DSA");
        elist4.Ehead = elist4.addsub("CN");
        MAP.put(rnode4, elist4.Ehead);
        Rnode rnode5 = Rlist.addstud("arslan", 44);
        LMS elist5 = new LMS();
        MAP.put(rnode5, elist5.Ehead);
        System.out.println("registration list:");
        Rlist.show();
        Rnode present = Rlist.searchRnode(45);
        Rlist.delstud(30);
        MAP.remove(rnode3);
        System.out.println(MAP);
        Rlist.show();
        if (present!=null){
            System.out.println(present.name);
        }
        else {
            System.out.println(present);
        }
        System.out.println("MAP :");
        System.out.println(MAP);
        System.out.print("enrollments - abdullah : ");
        Rlist.showsub(MAP.get(rnode1));
        System.out.print("enrollments - noman : ");
        Rlist.showsub(MAP.get(rnode4));
       
    }
}