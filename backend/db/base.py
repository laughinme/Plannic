from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    
    def __repr__(self):
        cls_name = self.__class__.__name__
        column_names = self.__mapper__.columns.keys()
        
        values = ', '.join(f"{name}={getattr(self, name)!r}" for name in column_names)
        return f"<{cls_name}({values})>"
    