import React from "react";
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import HoroscopeGenerator from "../HoroscopeGenerator";

// Simple smoke tests and interaction test

describe("HoroscopeGenerator", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it("renders form inputs and button", () => {
    render(<HoroscopeGenerator />);
    expect(screen.getByPlaceholderText("Név")).toBeTruthy();
    expect(screen.getByPlaceholderText("HH")).toBeTruthy();
    expect(screen.getByPlaceholderText("NN")).toBeTruthy();
    expect(
      screen.getByRole("button", { name: /Mutasd a horoszkópom/i })
    ).toBeTruthy();
  });

  it("validates inputs and shows error when missing", async () => {
    render(<HoroscopeGenerator />);
    const button = screen.getByRole("button", {
      name: /Mutasd a horoszkópom/i,
    });
    fireEvent.click(button);

    expect(await screen.findByText(/Adj meg egy nevet!/i)).toBeTruthy();
  });

  it("calls API and shows quote on success", async () => {
    const fakeResponse = { message: "Szia, ez a horoszkópod" };
    globalThis.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fakeResponse,
    });

    render(<HoroscopeGenerator />);

    fireEvent.change(screen.getByPlaceholderText("Név"), {
      target: { value: "Teszt" },
    });
    fireEvent.change(screen.getByPlaceholderText("HH"), {
      target: { value: "1" },
    });
    fireEvent.change(screen.getByPlaceholderText("NN"), {
      target: { value: "1" },
    });

    fireEvent.click(
      screen.getByRole("button", { name: /Mutasd a horoszkópom/i })
    );

    await waitFor(() => expect(globalThis.fetch).toHaveBeenCalled());
    expect(await screen.findByText(/Szia, ez a horoszkópod/i)).toBeTruthy();
  });
});
