__all__ = ["Album", "Artist", "Customer", "Employee", "Genre", "Invoice", "Invoiceline", "Mediatype", "Playlist", "Playlisttrack", "Track"]
from dataclasses import dataclass
from fastsql.core import UNSET
import datetime, decimal
@dataclass
class Album:
    AlbumId: int | None = UNSET
    Title: str | None = UNSET
    ArtistId: int | None = UNSET

@dataclass
class Artist:
    ArtistId: int | None = UNSET
    Name: str | None = UNSET

@dataclass
class Customer:
    CustomerId: int | None = UNSET
    FirstName: str | None = UNSET
    LastName: str | None = UNSET
    Company: str | None = UNSET
    Address: str | None = UNSET
    City: str | None = UNSET
    State: str | None = UNSET
    Country: str | None = UNSET
    PostalCode: str | None = UNSET
    Phone: str | None = UNSET
    Fax: str | None = UNSET
    Email: str | None = UNSET
    SupportRepId: int | None = UNSET

@dataclass
class Employee:
    EmployeeId: int | None = UNSET
    LastName: str | None = UNSET
    FirstName: str | None = UNSET
    Title: str | None = UNSET
    ReportsTo: int | None = UNSET
    BirthDate: datetime.datetime | None = UNSET
    HireDate: datetime.datetime | None = UNSET
    Address: str | None = UNSET
    City: str | None = UNSET
    State: str | None = UNSET
    Country: str | None = UNSET
    PostalCode: str | None = UNSET
    Phone: str | None = UNSET
    Fax: str | None = UNSET
    Email: str | None = UNSET

@dataclass
class Genre:
    GenreId: int | None = UNSET
    Name: str | None = UNSET

@dataclass
class Invoice:
    InvoiceId: int | None = UNSET
    CustomerId: int | None = UNSET
    InvoiceDate: datetime.datetime | None = UNSET
    BillingAddress: str | None = UNSET
    BillingCity: str | None = UNSET
    BillingState: str | None = UNSET
    BillingCountry: str | None = UNSET
    BillingPostalCode: str | None = UNSET
    Total: decimal.Decimal | None = UNSET

@dataclass
class Invoiceline:
    InvoiceLineId: int | None = UNSET
    InvoiceId: int | None = UNSET
    TrackId: int | None = UNSET
    UnitPrice: decimal.Decimal | None = UNSET
    Quantity: int | None = UNSET

@dataclass
class Mediatype:
    MediaTypeId: int | None = UNSET
    Name: str | None = UNSET

@dataclass
class Playlist:
    PlaylistId: int | None = UNSET
    Name: str | None = UNSET

@dataclass
class Playlisttrack:
    PlaylistId: int | None = UNSET
    TrackId: int | None = UNSET

@dataclass
class Track:
    TrackId: int | None = UNSET
    Name: str | None = UNSET
    AlbumId: int | None = UNSET
    MediaTypeId: int | None = UNSET
    GenreId: int | None = UNSET
    Composer: str | None = UNSET
    Milliseconds: int | None = UNSET
    Bytes: int | None = UNSET
    UnitPrice: decimal.Decimal | None = UNSET

