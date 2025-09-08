package com.excess2need.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.excess2need.backend.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByEmail(String email);
}
