from paulistrings import Circuit, PauliString, PauliSum, PauliTerms, p, pt


def test_p_is_a_string_and_pt_is_terms() -> None:
    assert isinstance(assert_type(p("XYZ"), PauliString), PauliString)
    assert isinstance(assert_type(pt("X", range(4)), PauliTerms), PauliTerms)
    assert isinstance(assert_type(pt("ZZ", [(0, 1), (1, 2)]), PauliTerms), PauliTerms)


def test_arithmetic_keeps_the_types() -> None:
    hamiltonian = -1.0 * pt("ZZ", [(0, 1)]) - 0.5 * pt("X", range(2))
    assert_type(hamiltonian, PauliTerms)
    assert isinstance(assert_type(PauliSum(2, hamiltonian), PauliSum), PauliSum)
    assert isinstance(assert_type(p("XY") * 2.0, PauliSum), PauliSum)


def test_rejected_calls_fail_at_runtime_and_statically() -> None:
    with pytest.raises(TypeError):
        p("ZZ", (0, 1))  # type: ignore[call-arg]
    with pytest.raises(TypeError):
        p("X") * p("Z")  # type: ignore[operator]
    with pytest.raises(ValueError):
        Circuit(1).trotter(pt("X", 0), 0.1, order=3)  # type: ignore[arg-type]