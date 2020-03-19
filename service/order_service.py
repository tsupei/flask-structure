# -*- coding: utf-8 -*-
import logging

class OrderService(object):
    def __init__(self, automaton):
        self.automaton = automaton

    def order(self, sentence):
        orders = [{
            "drink": "unknown",
            "ice": "unknown",
            "sugar": "unknown",
            "topping": "default"
        }]
        for end_index, (entity_tag, key_value) in self.automaton.iter(sentence):
            if entity_tag == "drink":
                if orders[-1]["drink"] == "unknown":
                    orders[-1]["drink"] = key_value
                else:
                    new_order = {
                        "drink": key_value,
                        "ice": "unknown",
                        "sugar": "unknown",
                        "topping": "default"
                    }
                    orders.append(new_order)
            elif entity_tag == "ice":
                orders[-1]["ice"] = key_value
            elif entity_tag == "sugar":
                orders[-1]["sugar"] = key_value
            end_index += 1
            start_index = end_index - len(key_value)
            print(start_index, end_index, key_value)
        return orders


