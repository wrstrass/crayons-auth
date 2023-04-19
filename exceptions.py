from fastapi import HTTPException, status


class HTTP_403(HTTPException):
    def __init__(self, detail=None, headers=None) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail=detail, headers=headers
        )


class HTTP_404(HTTPException):
    def __init__(self, detail=None, headers=None) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=detail, headers=headers
        )
