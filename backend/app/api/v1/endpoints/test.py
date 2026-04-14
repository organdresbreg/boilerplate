from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Any

router = APIRouter()


@router.get("/test")
async def test_endpoint() -> dict[str, str]:
    """Endpoint de prueba"""
    return {"message": "API v1 is working", "year": "2026"}
