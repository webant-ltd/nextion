command_failed_codes = {
    0x00: "Invalid instruction", 0x02: "Component ID invalid",
    0x03: "Page ID invalid", 0x04: "Picture ID invalid", 0x05: "Font ID invalid",
    0x11: "Baud rate setting invalid", 0x12: "Curve control ID number or channel number is invalid",
    0x1A: "Variable name invalid", 0x1B: "Variable operation invalid",
    0x1C: "Failed to assign", 0x1D: "Operate EEPROM failed", 0x1E: "Parameter quantity invalid",
    0x1F: "IO operation failed", 0x20: "Undefined escape characters", 0x23: "Too long variable name"
}


class CommandFailed(Exception):
    pass


class CommandTimeout(Exception):
    pass
