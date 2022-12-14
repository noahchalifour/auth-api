//
// Client.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation
#if canImport(AnyCodable)
import AnyCodable
#endif

public struct Client: Codable, JSONEncodable, Hashable {

    public var id: UUID?
    public var name: String
    public var description: String?
    public var services: AnyCodable?
    public var dateCreated: Date?

    public init(id: UUID? = nil, name: String, description: String? = nil, services: AnyCodable? = nil, dateCreated: Date? = nil) {
        self.id = id
        self.name = name
        self.description = description
        self.services = services
        self.dateCreated = dateCreated
    }

    public enum CodingKeys: String, CodingKey, CaseIterable {
        case id
        case name
        case description
        case services
        case dateCreated = "date_created"
    }

    // Encodable protocol methods

    public func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encodeIfPresent(id, forKey: .id)
        try container.encode(name, forKey: .name)
        try container.encodeIfPresent(description, forKey: .description)
        try container.encodeIfPresent(services, forKey: .services)
        try container.encodeIfPresent(dateCreated, forKey: .dateCreated)
    }
}

