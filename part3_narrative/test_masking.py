from masking import alias_for, assert_no_raw_names_leak


reseller_names = [
    "Mumbai Reseller 1",
    "Mumbai Reseller 4",
    "Hyderabad Reseller 6",
    "Lucknow Reseller 6",
    "Jaipur Reseller 5",
]


# Check alias format
assert alias_for("RS019") == "ALIAS-19"
assert alias_for("RS006") == "ALIAS-06"


# Negative case: raw reseller name should fail
raw_narrative = "Mumbai Reseller 1 had the highest revenue."
assert assert_no_raw_names_leak(raw_narrative, reseller_names) is False


# Positive case: masked narrative should pass
masked_narrative = (
    "ALIAS-19 is a top reseller in the West region. "
    "The reseller is referred to using an alias."
)
assert assert_no_raw_names_leak(masked_narrative, reseller_names) is True


print("All masking tests passed.")