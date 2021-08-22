import numpy as np
import matplotlib.pyplot as plt

message = "ZE KYV KFNE NYVIV Z NRJ SFIE CZMVU R DRE NYF JRZCVU KF JVR REU YV KFCU LJ FW YZJ CZWV ZE KYV CREU FW " \
          "JLSDRIZEVJ JF NV JRZCVU LG KF KYV JLE ‘KZC NV WFLEU R JVR FW XIVVE REU NV CZMVU SVEVRKY KYV NRMVJ ZE FLI " \
          "PVCCFN JLSDRIZEV NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV NV RCC CZMV ZE R " \
          "PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV REU FLI WIZVEUJ RIV RCC RSFRIU DREP DFIV FW KYVD CZMV " \
          "EVOK UFFI REU KYV SREU SVXZEJ KF GCRP NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV" \
          "NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV (WLCC JGVVU RYVRU DI. GRIBVI, " \
          "WLCC JGVVU RYVRU WLCC JGVVU RYVRU ZK ZJ, JVIXVREK RTKZFE JKRKZFE, RTKZFE JKRKZFE RPV, RPV, JZI, " \
          "WZIV TRGKRZE, TRGKRZE) RJ NV CZMV R CZWV FW VRJV VMVIPFEV FW LJ YRJ RCC NV EVVU (YRJ RCC NV EVVU) JBP FW " \
          "SCLV (JBP FW SCLV) REU JVR FW XIVVE (REU JVR FW XIVVE) ZE FLI PVCCFN JLSDRIZEV (ZE FLI PVCCFN, JLSDRIZEV, " \
          "YR YR) NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV NV RCC CZMV ZE R PVCCFN " \
          "JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, " \
          "PVCCFN JLSDRIZEV NV RCC CZMV ZE R PVCCFN JLSDRIZEV PVCCFN JLSDRIZEV, PVCCFN JLSDRIZEV"


Caps_message = message.upper()
l = len(message)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
# Returns a dictionary with keys of single letters and values of the
# count of how many times they appear in the message parameter.

    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

print(getLetterCount(message))


# bar plot stuff
x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
english_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

message_freq = [100*Caps_message.count("A")/len(message), 100*Caps_message.count("B")/len(message), 100*Caps_message.count("C")/len(message), 100*Caps_message.count("D")/len(message), 100*Caps_message.count("E")/len(message), 100*Caps_message.count("F")/len(message), 100*Caps_message.count("G")/len(message), 100*Caps_message.count("H")/len(message), 100*Caps_message.count("I")/len(message), 100*Caps_message.count("J")/len(message), 100*Caps_message.count("K")/len(message), 100*Caps_message.count("L")/len(message), 100*Caps_message.count("M")/len(message), 100*Caps_message.count("N")/len(message), 100*Caps_message.count("O")/len(message), 100*Caps_message.count("P")/len(message), 100*Caps_message.count("Q")/len(message), 100*Caps_message.count("R")/len(message), 100*Caps_message.count("S")/len(message), 100*Caps_message.count("T")/len(message), 100*Caps_message.count("U")/len(message), 100*Caps_message.count("V")/len(message), 100*Caps_message.count("W")/len(message), 100*Caps_message.count("X")/len(message), 100*Caps_message.count("Y")/len(message), 100*Caps_message.count("Z")/len(message)]

width = 0.4
plt.bar(x, english_freq, width=width)
plt.bar(np.arange(len(message_freq)) + width, message_freq, width=width)
plt.xlabel("letter")
plt.ylabel("relative frequency")
plt.show()

