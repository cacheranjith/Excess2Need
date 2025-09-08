package com.excess2need.backend.controller;

import com.excess2need.backend.model.User;
import com.excess2need.backend.service.AuthService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @Autowired
    private AuthService authService;

    @PostMapping("/register")
    public String register(@RequestBody User user) {
        return authService.registerUser(user);
    }

    @GetMapping("/login")
    public String login() {
        return "Login successful!";
    }
}
