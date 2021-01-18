class Parking:
    rate_data = dict()
    day_week_map = {1: 'sun',
                    2: 'mon',
                    3: 'tue',
                    4: 'wed',
                    5: 'thu',
                    6: 'fri',
                    7: 'sat'}
    total_collection = 0

    def __init__(self, morning_disc, evening_disc):
        self.rate_data['sun'] = [8, 2, 2]
        self.rate_data['mon'] = [2, 10, 2]
        self.rate_data['tue'] = [2, 10, 2]
        self.rate_data['wed'] = [2, 10, 2]
        self.rate_data['thu'] = [2, 10, 2]
        self.rate_data['fri'] = [2, 10, 2]
        self.rate_data['sat'] = [4, 3, 2]
        self.MORNING_DISCOUNTED_FACTOR = 1 - (morning_disc // 100)
        self.EVENING_DISCOUNTED_FACTOR = 1 - (evening_disc // 100)
        self.MODULATOR = 11

    def is_valid_fpn(self, fpn):
        """ Validates the Frequent Parking Number"""
        received_key = fpn % 10
        generated_key = 0
        generator = 2

        fpn //= 10
        while fpn > 0:
            generated_key += (fpn % 10 * generator)
            generator += 1
            fpn //= 10

        generated_key %= self.MODULATOR

        if (self.MODULATOR - generated_key) == received_key:
            return True
        else:
            return False

    def get_basic_core_price(self, day, arrival_time, parking_duration):
        if arrival_time >= 16:
            core_price = self.rate_data[day][2]
        else:
            core_price = self.rate_data[day][1] * parking_duration

        return core_price

    def get_improvised_core_price(self, day, arrival_time, parking_duration):
        if (arrival_time + parking_duration < 16) or (arrival_time >= 16):
            core_price = self.get_basic_core_price(day, arrival_time, parking_duration)
        else:
            core_price = self.get_basic_core_price(day, arrival_time, 16 - arrival_time)
            if 16 - arrival_time > 0:
                core_price += self.get_basic_core_price(day, 16, 16 - arrival_time)

        return core_price

    def get_parking_price(self, day, arrival_time, parking_duration, task, fpn=None):
        if task == 1:
            parking_price = self.get_basic_core_price(day, arrival_time, parking_duration)
        else:
            parking_price = self.get_improvised_core_price(day, arrival_time, parking_duration)

        if fpn and self.is_valid_fpn(fpn):
            if arrival_time < 16:
                print("Dear member, welcome. Now you can enjoy " + str(
                    int((1 - self.MORNING_DISCOUNTED_FACTOR) * 100)) + "% discount")
                parking_price *= self.MORNING_DISCOUNTED_FACTOR
            else:
                print("Dear member, welcome. Now you can enjoy " + str(
                    int((1 - self.EVENING_DISCOUNTED_FACTOR) * 100)) + "% discount")
                parking_price *= self.EVENING_DISCOUNTED_FACTOR
        else:
            print("The Frequent Parking Number that you entered is incorrect! No discount is applied")

        return parking_price

    def main(self):
        day_of_week = input(
            "Enter a day of week.\nSunday \t 1\nMonday \t 2\nTuesday \t 3\nWednesday \t 4\nThursay \t 5\nFriday \t 6\nSaturday \t 6")
        if not day_of_week.isnumeric() or int(day_of_week) not in range(1, 8):
            print("Wrong day of the week entered. Please restart")
            return
        day_of_week = self.day_week_map[int(day_of_week)]

        arrival = input("Enter the time of your arrival. Our hours of operation 8:00 am to 12:00 am")
        if not arrival.isnumeric() or int(arrival) not in range(8, 24):
            print("We're sorry! We don't operate in those hours")
            return
        arrival = int(arrival)

        parking_duration = input("Enter the hours for which you wish to park your vehicle.\nYou arrived at " + str(
            arrival) + " and you have " + str(24 - arrival) + " hour(s) left")
        if not parking_duration.isnumeric():
            print("That time is invalid")
            return
        elif (arrival + int(parking_duration)) > 24:
            print("You cannot park here for that long")
            return
        parking_duration = int(parking_duration)

        parking_price = self.get_parking_price(day_of_week, arrival, parking_duration)
        print("Your parking charges are: " + str(parking_price))
        money = input("Please pay the exact amount + tips if any. The vending machine is unable to return any change")
        if not money.isnumeric():
            print("That is not a valid amount")
        else:
            money = int(money)
        self.total_collection += money

    def get_total_collection(self):
        return self.total_collection


if __name__ == '__main__':
    morning_discount = 10
    evening_discount = 50
    parking_object = Parking(morning_disc=morning_discount, evening_disc=evening_discount)
    print(parking_object.get_total_collection())

    # for _ in range(10):
    #   parking_object.main()
