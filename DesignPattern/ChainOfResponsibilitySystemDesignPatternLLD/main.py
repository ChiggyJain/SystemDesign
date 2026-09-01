
class NoteDispenser:

    def __init__(self, type_of_denomination_notes, total_denomination_notes_amount_available):
        self.type_of_denomination_notes = type_of_denomination_notes
        self.total_denomination_notes_amount_available = total_denomination_notes_amount_available
        self.next_note_dispenser_class_obj = None

    def set_next_note_dispenser(self, next_note_dispenser_class_obj):
        self.next_note_dispenser_class_obj = next_note_dispenser_class_obj

    def dispense(self, wWithdrawal_amount):
        count_of_type_of_denomination_notes_required = (wWithdrawal_amount//self.type_of_denomination_notes)
        # print(f"{self.type_of_denomination_notes}, {count_of_type_of_denomination_notes_required}")
        if count_of_type_of_denomination_notes_required>0 and self.total_denomination_notes_amount_available>0:
            self.total_denomination_notes_amount_available = self.total_denomination_notes_amount_available - (count_of_type_of_denomination_notes_required*self.type_of_denomination_notes)
            print(f"Dispense {count_of_type_of_denomination_notes_required} notes of Rs: {self.type_of_denomination_notes}")
            remainder = wWithdrawal_amount % self.type_of_denomination_notes
            # print(f"{self.type_of_denomination_notes}, {count_of_type_of_denomination_notes_required}, {self.total_denomination_notes_amount_available}, {remainder}")
            if remainder>0:
                if self.next_note_dispenser_class_obj:
                    self.next_note_dispenser_class_obj.dispense(remainder)
                else:
                    print(f"Cannot dispense remaining Rs: {remainder}")
        else:
            if self.next_note_dispenser_class_obj:
                self.next_note_dispenser_class_obj.dispense(wWithdrawal_amount)
            else:
                print(f"Cannot dispense remaining Rs: {wWithdrawal_amount}")




def main():

    # 2000 -> 500 -> 100
    h2000Obj = NoteDispenser(2000, 4000)
    h500Obj = NoteDispenser(500, 500)
    h100Obj = NoteDispenser(100, 500)
    h2000Obj.set_next_note_dispenser(h500Obj)
    h500Obj.set_next_note_dispenser(h100Obj)

    withdrawal_amounts = [3100]
    for eachWithdrawal_amount  in withdrawal_amounts:
        print("=====================================================")
        print(f"Withdrawing total amount of Rs: {eachWithdrawal_amount}")
        h2000Obj.dispense(eachWithdrawal_amount)
        print("=====================================================")
        


main()
